graph [
  node [
    id 0
    label 1
    disk 10
    cpu 3
    memory 4
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 4
    memory 16
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 1
    memory 3
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 3
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 3
    memory 14
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 155
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 152
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 131
  ]
  edge [
    source 1
    target 4
    delay 28
    bw 112
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 76
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 90
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 124
  ]
]
