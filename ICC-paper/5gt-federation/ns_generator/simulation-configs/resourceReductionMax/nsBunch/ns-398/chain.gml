graph [
  node [
    id 0
    label 1
    disk 6
    cpu 4
    memory 6
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 1
    memory 2
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 3
    memory 12
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 9
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 1
    memory 2
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 4
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 121
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 65
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 136
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 192
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 181
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 114
  ]
]
