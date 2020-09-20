graph [
  node [
    id 0
    label 1
    disk 4
    cpu 3
    memory 9
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 4
    memory 11
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 2
    memory 8
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 2
    memory 3
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 3
    memory 12
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 3
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 177
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 154
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 101
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 110
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 87
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 50
  ]
]
