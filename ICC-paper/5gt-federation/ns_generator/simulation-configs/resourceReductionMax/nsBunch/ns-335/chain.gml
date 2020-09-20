graph [
  node [
    id 0
    label 1
    disk 10
    cpu 2
    memory 16
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 3
    memory 16
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 1
    memory 13
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 2
    memory 16
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 2
    memory 8
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 4
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 135
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 129
  ]
  edge [
    source 0
    target 2
    delay 25
    bw 118
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 179
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 101
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 104
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 155
  ]
]
