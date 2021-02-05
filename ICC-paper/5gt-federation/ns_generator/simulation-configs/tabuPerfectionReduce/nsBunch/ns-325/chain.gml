graph [
  node [
    id 0
    label 1
    disk 3
    cpu 1
    memory 3
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 4
    memory 4
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 1
    memory 2
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 3
    memory 7
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 1
    memory 7
  ]
  node [
    id 5
    label 6
    disk 2
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
    delay 33
    bw 173
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 142
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 154
  ]
  edge [
    source 0
    target 3
    delay 30
    bw 88
  ]
  edge [
    source 1
    target 5
    delay 33
    bw 124
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 51
  ]
]
