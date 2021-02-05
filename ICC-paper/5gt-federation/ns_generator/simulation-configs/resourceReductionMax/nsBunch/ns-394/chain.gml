graph [
  node [
    id 0
    label 1
    disk 9
    cpu 3
    memory 7
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 2
    memory 16
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 12
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 2
    memory 6
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 1
    memory 12
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 1
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 92
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 114
  ]
  edge [
    source 1
    target 2
    delay 32
    bw 162
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 149
  ]
  edge [
    source 2
    target 4
    delay 29
    bw 109
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 198
  ]
]
