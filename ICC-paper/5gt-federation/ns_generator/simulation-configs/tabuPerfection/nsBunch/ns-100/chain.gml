graph [
  node [
    id 0
    label 1
    disk 4
    cpu 1
    memory 6
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 4
    memory 11
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 3
    memory 6
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 4
    memory 5
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 2
    memory 9
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 4
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 192
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 94
  ]
  edge [
    source 1
    target 2
    delay 32
    bw 96
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 111
  ]
  edge [
    source 1
    target 4
    delay 30
    bw 54
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 113
  ]
]
