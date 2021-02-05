graph [
  node [
    id 0
    label 1
    disk 10
    cpu 4
    memory 7
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 3
    memory 3
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 2
    memory 13
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 3
    memory 8
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 2
    memory 14
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 4
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 117
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 188
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 60
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 168
  ]
  edge [
    source 1
    target 4
    delay 31
    bw 191
  ]
  edge [
    source 2
    target 5
    delay 35
    bw 131
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 67
  ]
]
