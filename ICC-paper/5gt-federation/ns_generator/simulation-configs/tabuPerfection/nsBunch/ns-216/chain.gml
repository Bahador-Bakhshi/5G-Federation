graph [
  node [
    id 0
    label 1
    disk 5
    cpu 2
    memory 4
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 3
    memory 2
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 4
    memory 3
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 1
    memory 16
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 1
    memory 15
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 75
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 87
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 159
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 89
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 60
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 57
  ]
]
