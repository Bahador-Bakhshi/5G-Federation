graph [
  node [
    id 0
    label 1
    disk 9
    cpu 3
    memory 6
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 3
    memory 2
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 3
    memory 3
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 4
    memory 1
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 2
    memory 12
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 4
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 186
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 108
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 70
  ]
  edge [
    source 2
    target 3
    delay 32
    bw 141
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 123
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 198
  ]
]
